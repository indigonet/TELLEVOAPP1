import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ValrecuperarPageRoutingModule } from './valrecuperar-routing.module';

import { ValrecuperarPage } from './valrecuperar.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ValrecuperarPageRoutingModule
  ],
  declarations: [ValrecuperarPage]
})
export class ValrecuperarPageModule {}
