open System.Runtime.InteropServices

//create vector 1 and 2
let vector = CreateVector2(10.0, 0.0)
let vector2 = CreateVector2(0.0, 0.0)

// get X and Y of vectors 1
printfn"\nGet points of the first vector"
printfn $"The point X= {GetX(vector)} and point Y= {GetY(vector)}"


//get distance between two vectors
printfn"--------------------------------"
printfn"Distance"
let distance =distanceTo(vector,vector2)
printfn $"The distance is: {distance}"

//Move vector's points 
// !!!!!!
// Test 1 is being modified by vectorMovement
// !!!!!!

printfn"--------------------------------"
printfn"Move points"
printfn $"The before movement X= {GetX(vector)} and Y= {GetY(vector)}"
let move =vectorMovement(vector, -12.0,36.0)
printfn $"after movement X= {GetX(vector)} and Y= {GetY(vector)}"

//get midpoint from vector A to B
let Midpoint: Vector2 =midpoint(vector,vector2)

printfn"--------------------------------"
printfn"Get mid point"
printfn $"vector X= {GetX(vector)} Y={GetY(vector)}"
printfn $"vector2 X= {GetX(vector2)} Y={GetY(vector2)}"
printfn $"The mid point between vector and vector2 is: X= {GetX(Midpoint)} Y: {GetY(Midpoint)}"

//get percentage of the distance from vector A to B
let percentage: double =percentDistance(vector,vector2, 50)
let Newdistance =distanceTo(vector,vector2)

printfn"--------------------------------"
printfn"Get percentage between two vectors"
printfn $"vector X= {GetX(vector)} Y={GetY(vector)}"
printfn $"vector2 X= {GetX(vector2)} Y={GetY(vector2)}"
printfn $"The distance is: {Newdistance}"
printfn $"The point at 50 percent between vector and vector2 is: {percentage}"