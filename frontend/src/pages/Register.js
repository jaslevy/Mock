import { useState } from "react";
import LogRegPage from "../components/LogRegPage";
import { GoogleButton } from "../components/GoogleButton";

export default function Register() {
  const [buttonText, setButtonText] = useState("Register with Google");

  const handleGoogleRegister = () => {
    setButtonText("Clicked!");
  };

  return (
    <LogRegPage title="Join and Mock" subtitle="Get matched with a peer today">
      <GoogleButton text={buttonText} onClick={handleGoogleRegister} />
    </LogRegPage>
  );
}
