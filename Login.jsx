import { useState } from "react";
import axios from "axios";
import "./Login.css";

function Login() {

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const login = async () => {

    try {

      const response =
        await axios.post(

          "http://127.0.0.1:8000/auth/login",

          {
            email,
            password
          }
        );

      localStorage.setItem(

        "token",

        response.data.token
      );

      localStorage.setItem(

        "role",

        response.data.role
      );

      alert(
        "Login Successful"
      );

      window.location.href =
        "/dashboard";

    } catch (error) {

      console.log(error);

      if (
        error.response
      ) {

        alert(

          error.response.data.detail
        );

      } else {

        alert(
          "Backend Server Not Running"
        );
      }
    }
  };

  return (

    <div className="login-container">

      <div className="login-card">

        <h1>

          Automated AI Help Desk
          Reasoner

        </h1>

        <input

          type="email"

          placeholder="Enter Email"

          value={email}

          onChange={(e) =>
            setEmail(
              e.target.value
            )
          }
        />

        <input

          type="password"

          placeholder="Enter Password"

          value={password}

          onChange={(e) =>
            setPassword(
              e.target.value
            )
          }
        />

        <button
          onClick={login}
        >
          Login
        </button>

        <p>

          New User?

          <a
            href="/register"
          >
            Register Here
          </a>

        </p>

      </div>

    </div>
  );
}

export default Login;