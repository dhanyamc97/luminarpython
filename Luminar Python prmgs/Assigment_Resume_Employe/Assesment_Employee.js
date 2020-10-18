let empolyee=[

    {eid:100,name:"ajay",desig:"devop",join:1981,resign:2003},
    {eid:101,name:"vijay",desig:"devop",join:1992,resign:2008},
    {eid:102,name:"bijoy",desig:"ba",join:1999,resign:2007},
    {eid:103,name:"jhon",desig:"ba",join:1989,resign:2010},
    {eid:104,name:"danie",desig:"qa",join:2009,resign:2014},
    {eid:105,name:"lari",desig:"qa",join:1987,resign:2010},]
    
 // Q1: print all employee name and designation only

var e1=empolyee.map(obj=>[obj.desig,obj.name])
    console.log("Employee name and desig:",e1)
            // let result = empolyee.map(({ name, desig }) => ({name, desig}));
            //     console.log(result);


// qs2:print all employee details whose desig equals devop

var e2=empolyee.filter(ob => ob.desig=='devop')
    console.log(e2)

// qs3:print all employee details those who are woking in 80s  [*(>1980 & <1190)]

var e3=empolyee.filter(n => n.join>1980 & n.join<1990)
    console.log(e3)

// qs4:print all employee details those who have experience >9 years

var e4=empolyee.filter(n=>(n.resign-n.join)>9)
    console.log(e4)

// qs5:sort all employees based on theire joining year

var e4=empolyee.sort((a,b)=>a.join-b.join)
    console.log(e4)

