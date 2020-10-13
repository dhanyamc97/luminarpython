//sample input: HHHPPSDAAA
//expected op: 3H2P1S1D3A

var str= "HHHPPSDAAA"

var cnt={}
for (ch of str){
    if(ch in cnt){
        cnt[ch]+=1;
    }
    else{
        cnt[ch]=1;
    }

}
var out=""
//console.log(outpt)
for(key in cnt){
    console.log(key)
    console.log(cnt[key])
    out=out+cnt[key]+key
}
console.log(outpt)

//wordcount,recursive character