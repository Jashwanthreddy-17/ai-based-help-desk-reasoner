import { Link } from "react-router-dom";

function Dashboard() {

  const role =
    localStorage.getItem(
      "role"
    );

  return (

    <div
      style={{
        padding: "30px"
      }}
    >

      <h1>
        AI Help Desk Dashboard
      </h1>

      <hr />

      <h3>
        Logged In As:
        {" "}
        {role}
      </h3>

      <br />

      <Link to="/chat">

        <button>
          Open AI Chat
        </button>

      </Link>

      <br />
      <br />

         <Link to="/tickets">

  <button>

    View Tickets

  </button>

</Link>

      <br />
      <br />

      <button>

        Knowledge Base

      </button>

      <br />
      <br />

      {role === "admin" && (




 <Link to="/Admin">

  <button>

    Admin panel

  </button>

</Link>

      )}


    </div>
  );
}

export default Dashboard;