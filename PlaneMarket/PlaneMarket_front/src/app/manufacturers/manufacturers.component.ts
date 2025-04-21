import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Manufacturer } from '../models';
import {CommonModule} from "@angular/common";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";

@Component({
  selector: 'app-manufacturers',
  templateUrl: 'manufacturers.component.html',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule, ReactiveFormsModule],
})
export class ManufacturersComponent implements OnInit {
  manufacturers: Manufacturer[] = [];

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.getManufacturers().subscribe((data) => (this.manufacturers = data));
  }
}
