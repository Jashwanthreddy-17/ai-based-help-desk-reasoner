import {
 useEffect,
 useState
} from "react";

function TypingEffect({ text }) {

 const [display,
 setDisplay] = useState("");

 useEffect(() => {

   let i = 0;

   const timer =
   setInterval(() => {

     setDisplay(
       text.slice(0, i)
     );

     i++;

     if(i > text.length)
       clearInterval(timer);

   }, 15);

   return () =>
     clearInterval(timer);

 }, [text]);

 return <p>{display}</p>;
}

export default TypingEffect;