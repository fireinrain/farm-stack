import TodoItem from "./TodoItem";

function TodoListView(props) {
    return (
        <div className="card text-white bg-dark" style={{paddingTop:'20px',paddingLeft:'5px'}}>
            <ol style={{fontSize:'2em'}}>
                {
                    props.todoList.map(todoItem => <>
                        <li key={todoItem.title} style={{marginBottom:'-55px'}}><TodoItem todo={todoItem}/></li>
                        <hr></hr>


                    </>)
                }
            </ol>
        </div>
    )
}

export default TodoListView