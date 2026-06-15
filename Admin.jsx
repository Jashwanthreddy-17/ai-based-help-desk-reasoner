import { useEffect, useState } from "react";
import axios from "axios";

function Admin() {

  const [tickets, setTickets] =
    useState([]);

  useEffect(() => {

    loadTickets();

  }, []);

  const loadTickets = async () => {

    const response =
      await axios.get(
        "http://127.0.0.1:8000/tickets"
      );

    setTickets(
      response.data
    );
  };

  const updateStatus = async (
    id,
    status
  ) => {

    await axios.put(

      `http://127.0.0.1:8000/tickets/${id}`,

      {
        status
      }
    );

    loadTickets();
  };

  return (

    <div
      style={{
        padding: "30px"
      }}
    >

      <h1>
        Admin Panel
      </h1>

      <table
        border="1"
        cellPadding="10"
        width="100%"
      >

        <thead>

          <tr>

            <th>ID</th>
            <th>Title</th>
            <th>Status</th>
            <th>Action</th>

          </tr>

        </thead>

        <tbody>

          {tickets.map(ticket => (

            <tr key={ticket.id}>

              <td>{ticket.id}</td>

              <td>{ticket.title}</td>

              <td>{ticket.status}</td>

              <td>

                <button
                  onClick={() =>
                    updateStatus(
                      ticket.id,
                      "IN_PROGRESS"
                    )
                  }
                >
                  In Progress
                </button>

                {" "}

                <button
                  onClick={() =>
                    updateStatus(
                      ticket.id,
                      "CLOSED"
                    )
                  }
                >
                  Close
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Admin;