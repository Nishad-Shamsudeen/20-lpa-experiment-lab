import dotenv from "dotenv";
dotenv.config();

const PORT = process.env.PORT || 3000
import express from "express";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json())

let users = [
  { id: 1, name: "Nishad", NetWorth: "1 Trillion" },
  { id: 2, name: "Naima", NetWorth: "100 Billion" },
];


app.get("/", (req, res) => {
  res.send("Hello Nishad you are Back on Track.");
});

app.get("/users",(  req,res)=>{
    res.json(users)
})

app.post("/users",(req,res)=>{
    const newUser = req.body
    users.push(newUser)
    res.status(201).json(newUser)
})

app.listen(PORT, function () {
  console.log(`Server is Running on PORT ${PORT}`);
});
