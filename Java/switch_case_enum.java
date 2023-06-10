private enum FooNum {
  //Options for your enum
  A, 
  B
  }

public void foo(FooNum fooNum){

switch(fooNum){
	case A:		
	    //you selected A
    	break;
  	case B:
    	//you selected B
		break;  
  	default:			
	    //do some stuff
	    break;
	} 
}
