import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITaskList, ITask, IAuthResponse } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public taskLists: ITaskList[] = [];
  public tasks: ITask[] = [];
  public loading = false;
  public showTasks = false;
  public name: any = '';
  public logged = false;

  public login: any = '';

  public password: any = '';




  constructor(private provider: ProviderService) {
  }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
    if (this.logged) {
      this.provider.getTaskLists().then(res => {
        this.taskLists = res;
      });
    }
  }

  getTasks(taskList: ITaskList) {
    this.provider.getTasks(taskList).then(res => {
      this.tasks = res;
      this.showTasks = true;
    });
  }

  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.taskLists.push(res);
      });
    }
  }

  updateTaskList(t: ITaskList) {
    this.provider.updateTaskList(t).then(res => {
      console.log(t.name + 'updated');
    });
  }

  deleteTaskList(t: ITaskList) {
    this.provider.deleteTaskList(t.id).then(res => {
      console.log(t.name + 'deleted!');
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }
  logIn() {
    if (this.login !== '' && this.password !== '') {
      this.provider.logIn(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);

        this.logged = true;

        this.provider.getTaskLists().then(r => {
          this.taskLists = r;
        });

      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.logged = false;
    });
  }
}
