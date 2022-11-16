//File and path you want to create and write to
string fileName = @"C:\Temp\Temp.txt"; 
//Check if the file exists
if (!File.Exists(fileName)) 
{
    // Create the file and use streamWriter to write text to it.
	//If the file existence is not check, this will overwrite said file.
	//Use the using block so the file can close and vairable disposed correctly
    using (StreamWriter writer = File.CreateText(fileName)) 
    {
        writer.WriteLine("Hello World");
    }	
}
