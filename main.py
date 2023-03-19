# python3

def parallel_processing(n, m, data):
    output = []
    taken = []
    time = []
    lastingt = []
    for i in range(n):
      time.append(0)
      taken.append(0)
      lastingt.append(0)
      a = 0
    makelifeeasaier(taken, data, i, a, lastingt, output, time, n, m)
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output


def makelifeeasaier(taken, data, i, a, lastingt, output, time, n, m):
  for i in range(m):
    while True: 
      if (taken[a]!=0):
        if(time[a]==taken[a]):
          time[a] = 0 
          taken[a] =0;
        else:
          time[a] = time[a]+1
          lastingt[a] = lastingt[a]+1
          if a==n-1:
            a=0
          else:
            a = a+1
      else:
        taken[a] = data[i]
        output.append((a, lastingt[a]))
        break;
        
            
  return output;
    

def main():
    text = input()
    text2 = input()
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, text.split())
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, text2.split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i, j in result:
      print(i,j)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

