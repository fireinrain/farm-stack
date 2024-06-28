import './App.css';
import React, {useState, useEffect} from "react";
import axios from "axios";
import 'bootstrap/dist/css/bootstrap.min.css'
import TodoListView from "./components/TodoListView";


function App() {
    const [todoList, setTodoList] = useState([{}])
    const [title, setTitle] = useState("")
    const [desc, setDesc] = useState("")

    // read all todos
    useEffect(() => {
        axios.get("http://localhost:8000/api/todo")
            .then(response => {
                setTodoList(response.data)
            })
    }, []);

    //post a todos-task
    const addTodoHandler = () => {
        if (title === '' || title === null || desc === null) {
            alert("Please fill the input title and description")
            return
        }
        axios.post("http://localhost:8000/api/todo", {
            'title': title, 'description': desc
        }).then(response => {
            console.log(response)
        })
    }


    return (
        <div className="AppContainer">
            <div className="App list-group-item justify-content-center align-items-center mx-auto"
                 style={{width: "960px", background: "white", marginTop: "15px"}}>
                <h1 className="card text-white bg-primary mb-1" style={{maxWidth: "60rem"}}>Task Manager</h1>
                <h6 className="card text-white bg-primary mb-3">FastAPI--React--Mongodb</h6>

                <div className="card-body">
                    <h4 className="card text-white bg-dark">Add Your Tasks Below</h4>

                    <input type="text" className="mb-2 form-control titleIn" placeholder="请输入任务标题"
                           onChange={event => setTitle(event.target.value)}/>
                    <input type="text" className="mb-2 form-control desIn" placeholder="请输入任务描述"
                           onChange={event => setDesc(event.target.value)}/>
                    <button className="btn btn-outline-primary mx-2 mb-3"
                            style={{borderRadius: "50px", fontWeight: "bold"}} onClick={addTodoHandler}>添加任务
                    </button>
                    <h4 className="card text-white bg-dark">待办任务列表</h4>
                    <div>
                        <TodoListView todoList={todoList}/>
                    </div>
                </div>

                <h6 className="card text-dark bg-warning py-1 mb-0">
                    Copyright 2024, All rights reserved &copy;
                </h6>
            </div>
        </div>
    );
}

export default App;
