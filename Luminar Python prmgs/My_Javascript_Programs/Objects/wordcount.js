var line="hai hello hai hello"

var words=line.split(" ")
console.log(words)

dict={}

for(word of words){

    if(word in dict){

        dict[word]+=1
        }
    else{

        dict[word]=1
        }
}

console.log(dict)
