arr = uninitialized UInt8[32]
 
arr[0] = 183
arr[1] = 226
arr[2] = 63
arr[3] = 210
arr[4] = 52
arr[5] = 236
arr[6] = 123
arr[7] = 223
arr[8] = 62
arr[9] = 152
arr[10] = 50
arr[11] = 111
arr[12] = 180
arr[13] = 191
arr[14] = 242
arr[15] = 253
arr[16] = 55
arr[17] = 181
arr[18] = 188
arr[19] = 226
arr[20] = 33
arr[21] = 197
arr[22] = 195
arr[23] = 179
arr[24] = 203
arr[25] = 168
arr[26] = 30
arr[27] = 17
arr[28] = 183
arr[29] = 50
arr[30] = 15
arr[31] = 71
 
rand = Random::PCG32.new(69)
c=0
while c < 32
  arr[c] ^= rand.rand(UInt8)
  c += 1
end
 
s = String.build do |io|
  arr.each do |number|
    io.write_byte number.to_u8
  end
end
puts s