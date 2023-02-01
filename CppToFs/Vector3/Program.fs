//Create vectors
let FstVector= CreateVector3(0.0, 0.0, 0.0)
let SndVector= CreateVector3(1.0, 2.0, 3.0)

//Get values
printfn"Get values"
printfn $"The before movement X= {GetX(SndVector)} and Y= {GetY(SndVector)} and Z={GetZ(SndVector)}"

//Get distance
let distance=distanceTo(FstVector,SndVector)
printfn"______________________________________________"
printfn"Get Distance"
printfn $"The Distance between the first and second vector is: {distance}"

//Move the first vector +1 to each point
let move=vectorMovement(FstVector,1.0,1.0,1.0)
printfn"______________________________________________"
printfn"Move the first vector +1 to each point"
printfn $"The Vector 1 was at X=0, Y=0 and Z=0 \nIt is now X= {GetX(FstVector)} and Y= {GetY(FstVector)} and Z={GetZ(FstVector)} "

//Get the midpoint between the two vectors
let Midpoint=midpoint(FstVector,SndVector)
printfn"______________________________________________"
printfn"Get the midpoint between the two vectors"
printfn $"The midpoint between the first and second vector is X= {GetX(Midpoint)} and Y= {GetY(Midpoint)} and Z={GetZ(Midpoint)} "

//Get the distance between the two vectors divised by a percentage
let percentage: double =percentDistance(FstVector,SndVector, 50)
let fullDistance=distanceTo(FstVector,SndVector)

printfn"______________________________________________"
printfn"Get the distance between the two vectors divised by a percentage"
printfn $"The distance between the first and second vector at 50 percent is: {percentage}"
printfn $"And the full distanc is: {fullDistance}"

