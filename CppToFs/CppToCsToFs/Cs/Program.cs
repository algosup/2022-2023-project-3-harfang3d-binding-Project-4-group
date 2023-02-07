using System.Runtime.InteropServices;
using System;
namespace Wrapper
{

    class Vectors
    {

        [StructLayout(LayoutKind.Sequential)]
        public struct Vector2
        {
            public int x;
            public int y;
        }
        [DllImport("compiled.dll")]
        public static extern Vector2 Vector2_Constructor(double x, double y);

        [DllImport("compiled.dll")]
        public static extern double distanceTo(Vector2 pos);

        [DllImport("compiled.dll")]
        public static extern void vectorMovement(double plusx, double plusy);


        // double distance = vector2.distanceTo(new Vector2(10, 20));

        static void Main(string[] args)
        {
            Vector2 v1 = Vector2_Constructor(0.0, 0.0);
            Console.WriteLine(v1);
        }

    }

}