
# SAP 인턴 테스트
"""

"""
def nonRepeatedChar(compString):
	# Write your code here
  count = 0
  for i in range(ord('a'), ord('z')+1):
    tmp = compString.count(chr(i))
    if tmp == 1:
      count += 1
      
  if not compString:
    print(0)
  elif count == 0:
    print(0)

  return count

def main():
	#input for compString
	compString = str(input())
	
	
	result = nonRepeatedChar(compString)
	print(result)	

if __name__ == "__main__":
	main()