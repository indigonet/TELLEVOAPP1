import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ValrecuperarPage } from './valrecuperar.page';

const routes: Routes = [
  {
    path: '',
    component: ValrecuperarPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ValrecuperarPageRoutingModule {}
