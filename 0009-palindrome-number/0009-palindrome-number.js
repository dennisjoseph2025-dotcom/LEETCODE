/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
   let a =x;
   let b = [];
   while(a>0){
    b.push(a%10);
    a=Math.floor(a/10);
   } 
   b=b.join("")
   if(x==0){
    return true
   }
   else if(b==x){
    return true
   }
   else{
    return false
   }
};