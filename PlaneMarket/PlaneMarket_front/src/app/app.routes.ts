import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ManufacturersComponent } from './manufacturers/manufacturers.component';
import { PlanesComponent } from './planes/planes.component';
import { OrdersComponent } from './orders/orders.component';
import { AppComponent } from './app.component';

export const routes: Routes = [
    { path: '', component: PlanesComponent },
    { path: 'login', component: LoginComponent },
    { path: 'manufacturers', component: ManufacturersComponent },
    { path: 'planes', component: PlanesComponent },
    { path: 'orders', component: OrdersComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
