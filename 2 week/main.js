function createTask (){
    var input = document.getElementById('text');
    var text=input.value;
    if(!text){
        alert('Type a description of a new task');
        return;
    }

    var task=document.createElement('div');
    task.className='task';

    var check=document.createElement('div');
    check.className='check';
    var chkBox=document.createElement('input');
    chkBox.type='checkbox';
    chkBox.onchange=tickTask;

    check.appendChild(chkBox);
    task.appendChild(check);

    var ext=document.createElement('div');
    ext.className='delete';
    var del=document.createElement('input');
    del.type='image';
    del.src='bin.png';
    del.onclick=deleteTask;

    ext.appendChild(del);
    task.appendChild(ext);

    var taskText=document.createElement('p');
    taskText.innerHTML=text;

    task.appendChild(taskText);

    document.getElementById('task').appendChild(task);
    input.value='';
}

function tickTask(e){
    var checkbox=e.target;
    var text=checkbox.parentElement.parentElement.childNodes[2];

    if(checkbox.checked){
    text.style.textDecoration = 'line-through';
  }
    else {
    text.style.textDecoration = 'none';
    }
}
function deleteTask(e) {
    var task=e.target.parentElement.parentElement;
    var tasks=task.parentElement;
    tasks.removeChild(task);
}





