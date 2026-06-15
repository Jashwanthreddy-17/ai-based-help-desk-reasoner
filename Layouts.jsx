import { Link } from "react-router-dom";

function Layout({ children }) {

  return (

    <div style={{display:"flex"}}>

      <div
        style={{
          width:"250px",
          height:"100vh",
          background:"#111827",
          color:"white",
          padding:"20px"
        }}
      >

        <h2>AI Help Desk</h2>

        <hr/>

        <p><Link to="/dashboard">Dashboard</Link></p>

        <p><Link to="/chat">Chat</Link></p>

        <p><Link to="/tickets">Tickets</Link></p>

        <p><Link to="/admin">Admin</Link></p>

      </div>

      <div
        style={{
          flex:1,
          padding:"30px",
          background:"#f3f4f6"
        }}
      >
        {children}
      </div>

    </div>
  );
}

export default Layout;