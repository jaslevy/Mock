import LogRegPage from "../components/LogRegPage";
import { GoogleButton } from "../components/GoogleButton";
export default function Register() {
  return (
    <LogRegPage title="Join and Mock"subtitle="Get matched with a peer today">
        <GoogleButton text="Register with Google" />
    </LogRegPage>
  );
}

