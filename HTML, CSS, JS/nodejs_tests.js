//Node.js 10.14.0
//Plain Javascript and Node.js is supported
// html/css is not supported here 


class studyFromHome{
  constructor(subject){
    this.object = "JavaScript, week 10 notes"
  }
    readNotes(){
      return "I am reading notes on " + this.object;
    }
    writeNotes(){
      return "I am writing notes on " + this.object;
      
    }
    doAssignment(){
      return "I am ready and writing notes, I do the assignment " + this.object
    }
     }
     studyFromHome = new studyFromHome("JavaScript")
     
     console.log(studyFromHome.readNotes())
     console.log(studyFromHome.writeNotes())
     console.log(studyFromHome.doAssignment())
    
    
