class Book{

    constructor(id,name,pageno,price){
        this.id=id;
        this.name=name;
        this.pageno=pageno;
        this.price=price;
    }

    getBook(){
        console.log(this.name);
        console.log(this.id)
    }
}

let obj=new Book(1,"text1",001,200);
let obj1=new Book(1,"text2",002,250);
let obj2=new Book(1,"text3",003,300);
let obj3=new Book(1,"text4",004,350);

var arr=[]
arr.push(obj)
arr.push(obj1)
arr.push(obj2)
arr.push(obj3)


// print all books with price > 250

var arrlen = arr.length;
for(var i=0;i<arrlen;i++){
    console.log(arrlen[i])
    console.log(arr[i])
}

//get book obj which have highest price

//print all bookname to uppercase
