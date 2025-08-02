import { Routes } from '@angular/router';

export const routes: Routes = [
   {
    path: '',
    pathMatch: 'full',
    redirectTo: 'login'
  },
  {
    path: 'login',
    loadComponent: () => import('./components/login/login').then(m => m.Login)
  },
  {
    path: 'dashboard',
    loadComponent: () => import('./components/dashboard/dashboard').then(m => m.Dashboard),
    children: [
      {
        path: '',
        loadComponent: () => import('./components/home/home').then(m => m.Home)
      },
      {
        path: 'mytickets',
        loadComponent: () => import('./components/myticket/myticket').then(m => m.Myticket)
      },
      {
        path: 'alltickets',
        loadComponent: () => import('./components/alltickets/alltickets').then(m => m.Alltickets)
      },
      {
        path: 'submitticket',
        loadComponent: () => import('./components/submitticket/submitticket').then(m => m.Submitticket)
      }
    ]
  }
 
];
