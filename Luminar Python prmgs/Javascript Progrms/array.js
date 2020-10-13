var num=[10,20,30,40,50]

console.log(num[1])

num[0]=100
console.log(num)

for ( item of num){
    console.log(item)
}

// for adding a number to a array

num.push(200);
console.log(num)

//search for a number in array
var flag=0
var x = 100
for(item of num){
    if(item==x){
        flag+=1;
        break;    
    }
    else{
        flag=0;   
    }
}    
if(flag>0){
    console.log("Item found");
}
else{
    console.log("Item not found");
}    

