import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {ITaskList, ITask, IAuthResponse} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }

  getTasks(taskList: ITaskList): Promise<ITask[]> {
    return this.get(`http://localhost:8000/api/task_lists/${taskList.id}/tasks/`, {});
  }

   createTaskList(n: any): Promise<ITaskList> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: n
    });
   }

  updateTaskList(taskLists: ITaskList): Promise<ITaskList> {
    return this.put(`http://localhost:8000/api/task_lists/${taskLists.id}/`, {
      name: taskLists.name
     });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }

  logIn(login: any, passwordd: any): Promise<IAuthResponse> {
    return this.post(`http://localhost:8000/api/login/`, {
      username: login,
      password: passwordd
    });
  }

  logout(): Promise<any> {
    return this.post(`http://localhost:8000/api/logout/`, {});
  }
}
