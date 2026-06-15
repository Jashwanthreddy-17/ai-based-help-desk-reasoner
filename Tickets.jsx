import { useEffect, useState } from "react";
import axios from "axios";

function Tickets() {

  const [tickets, setTickets] =
    useState([]);

  useEffect(() => {

    loadTickets();

  }, []);

  const loadTickets = async () => {

    try {

      const response =
        await axios.get(
          "http://127.0.0.1:8000/tickets"
        );

      setTickets(
        response.data
      );

    } catch (error) {

      console.log(error);

      alert(
        "Failed to load tickets"
      );
    }
  };

  return (

    <div
      style={{
        padding: "30px"
      }}
    >

      <h1>
        Support Tickets
      </h1>

      <table
        border="1"
        cellPadding="10"
        style={{
          width: "100%"
        }}
      >

        <thead>

          <tr>

            <th>ID</th>

            <th>Title</th>

            <th>Status</th>

            <th>Priority</th>

          </tr>

        </thead>

        <tbody>

          {tickets.map(ticket => (

            <tr
              key={ticket.id}
            >

              <td>
                {ticket.id}
              </td>

              <td>
                {ticket.title}
              </td>

              <td>
                {ticket.status}
              </td>

              <td>
                {ticket.priority}
              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Tickets;