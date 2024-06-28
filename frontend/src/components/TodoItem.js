import axios from "axios";
import React from "react"

function TodoItem(props) {
    const deleteTodoHandler = (title) => {
        axios.delete(`http://localhost:8000/api/todo/${title}`)
            .then(response => console.log(response))
    }
    return (
        <div>
            <p>
                <span style={{fontWeight: "bold,underline"}}>{props.todo.title}:</span>
                {props.todo.description}
                <button className="btn btn-lg btn-danger my-2 mx-2" style={{borderRadius: '40px',width:'40px',height:'40px'}}
                        onClick={() => deleteTodoHandler(props.todo.title)}></button>
            </p>
            <br></br>

        </div>
    )
}

export default TodoItem