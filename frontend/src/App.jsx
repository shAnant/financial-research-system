import { useEffect, useState } from "react";
import api from "./services/api";

function App() {

  const [msg, setMsg] = useState("");

  useEffect(() => {
    api.get("/")
      .then(res => setMsg(res.data.message))
      .catch(err => console.log(err));
  }, []);

  return (
    <>
      <h1>{msg}</h1>
    </>
  );
}

export default App;