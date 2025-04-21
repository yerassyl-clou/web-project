import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import {CommonModule} from "@angular/common";
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-navbar',
  templateUrl: 'navbar.component.html',
  standalone: true,
  styleUrls: ['navbar.component.css'],
  imports: [CommonModule, FormsModule]
})
export class NavbarComponent {
  constructor(public auth: AuthService) {}

  logout(): void {
    this.auth.logout();
  }
}
