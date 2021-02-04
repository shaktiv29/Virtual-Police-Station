# import socket
# import struct
#
# def main():
#     conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))
#     while True:
#         raw_data, addr = conn.recvfrom()
#         dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
#         print("\nEthernet Frame:")
#         print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))
#
# def ethernet_frame(data):
#     dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
#     return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]
# def get_mac_addr(bytes_addr):
#     bytes_str = map('{:02x}'.format, bytes_addr)
#     mac_addr = ':'.join(bytes_str).upper()
#
# main()
import itertools
n = int(input())
ans = []
def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res
def sol(x,lis1,lis2):
    yo = 0
    max=0
    new = []
    ding = []
    for i in range(x-1):
        if lis1[i] != lis1[i+1]:
            yo=1
    if yo == 0:
        if(lis1[0]>lis2[0]):
            return (lis2[0]*x)
        else :
            return (lis1[0]*x)
    else :
        perml = permutList(lis2)
        for i in perml:
            l =0
            sum =0
            while(l<x):
                sum = sum+i[l]*lis1[l]
                l+=1
            if sum>max:
                new = i
        for i in range(x):
            if(lis1[i]>new[i]):
                ding.append(new[i])
            else :
                ding.append(lis1[i])
        sum = 0
        for i in ding:
            sum+=i
        return sum

for i in range(n):
    x = int(input())
    lis1 = input().split()
    lis2 = input().split()
    lis1 = [int(i) for i in lis1]
    lis2 = [int(i) for i in lis2]
    ans.append(sol(x,lis1,lis2))
for i in ans:
    print(i)
