var pattern ='abbbabbbababbacc'

var dict={}

for(char of pattern)

  if(char  in dict){
      console.log("First recursive character ",char)
      break

  }
  else{
    dict[char]=1

  }
