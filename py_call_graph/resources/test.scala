object MainObject {  
   def main(args: Array[String]) {  
        var result = functionExample()          // Calling function  
        val f1 = function1()
        val f2 = function2()
        val f3 = function3()
        println(result)  
    }  
    def functionExample() = {       // Defining a function  
          var a = 10  
          val f2 = function2()
          a  
    }  

    def function1() = {
        "abc"
    }
    def function2() = {
        "abc"
    }
    def function3() = {
        "abc"
    }
}  