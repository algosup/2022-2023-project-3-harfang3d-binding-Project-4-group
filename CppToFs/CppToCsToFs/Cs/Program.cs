using System.Runtime.InteropServices;

namespace Wrapper
{
    [StructLayout(LayoutKind.Sequential)]
    public struct Vector2
    {
        [MarshalAs(UnmanagedType.R8)]
        public double x;
        [MarshalAs(UnmanagedType.R8)]
        public double y;
    }

    public class Vectors
    {
        [DllImport("compiled.dylib")]
        public static extern Vector2 Create(double x, double y);

        [DllImport("compiled.dylib")]
        public static extern double distanceTo(Vector2 pos, Vector2 pos2);

        [DllImport("compiled.dylib")]
        public static extern double test(double x);

        [DllImport("compiled.dylib")]
        public static extern void vectorMovement(double plusx, double plusy);

        static void Main(string[] args)
        {
            // Vector2 vec1=Create(10.0,0.0);
            // Vector2 vec2=Create(0.0,0.0);
            // double dist=distanceTo(test, test2);
            Console.WriteLine("x="+Create(10.0,25.0).x+"\ny="+Create(20.0,40.0).y);
        }
    }
}
