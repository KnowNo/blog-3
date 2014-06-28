class GroovyUtils {
   def static dir(Object object) {
       println object.metaClass.methods*.name.sort().unique()  
   }
}