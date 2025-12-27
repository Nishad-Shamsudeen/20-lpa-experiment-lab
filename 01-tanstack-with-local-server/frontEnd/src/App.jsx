import "./App.css";
import BackupData from "./Components/BackupData";
import ListUsers from "./Components/ListUsers";
import { useUserListMutation } from "./Hooks/useUserList";

function App() {

  const { mutate ,data} = useUserListMutation()

  if(data){
    console.log("test mutate",data);
  }

  return (
    <>
      
      <button onClick={() => mutate()}>Add User</button>
      <h1>List Of Users</h1>
      {data && <p>{data.name}</p>}

      <BackupData />
      <ListUsers/>

    </>
  );
}

export default App;
