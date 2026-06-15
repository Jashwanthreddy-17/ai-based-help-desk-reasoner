import { useState } from "react";
import axios from "axios";

function Register() {

  const [form, setForm] = useState({

    name: "",

    email: "",

    password: "",

    role: "employee"
  });

  const register = async () => {

    try {

      await axios.post(
        "http://127.0.0.1:8000/auth/register",
        form
      );

      alert("Registered");

    } catch {

      alert("Failed");
    }
  };

  return (

    <div>

      <h2>Register</h2>

      <input
        placeholder="Name"
        onChange={(e) =>
          setForm({
            ...form,
            name: e.target.value
          })
        }
      />

      <br />

      <input
        placeholder="Email"
        onChange={(e) =>
          setForm({
            ...form,
            email: e.target.value
          })
        }
      />

      <br />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setForm({
            ...form,
            password: e.target.value
          })
        }
      />

      <br />

      <button onClick={register}>
        Register
      </button>

    </div>
  );
}

export default Register;