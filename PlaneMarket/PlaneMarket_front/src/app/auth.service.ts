import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { ApiService } from './api.service';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private accessTokenKey = 'access_token';
  private refreshTokenKey = 'refresh_token';
  private currentUserSubject = new BehaviorSubject<string | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  constructor(private api: ApiService) {
    const token = this.getAccessToken();
    if (token) {
      this.api.getCurrentUser().subscribe({
        next: (user) => this.currentUserSubject.next(user.username),
        error: () => this.logout(),
      });
    }
  }

  login(username: string, password: string): Observable<void> {
    return new Observable<void>((observer) => {
      this.api.login({ username, password }).subscribe({
        next: (res) => {
          this.setTokens(res.access, res.refresh);
          this.api.getCurrentUser().subscribe({
            next: (user) => {
              this.currentUserSubject.next(user.username);
              observer.next();
              observer.complete();
            },
            error: (err) => observer.error(err),
          });
        },
        error: (err) => observer.error(err),
      });
    });
  }

  logout(): void {
    const refresh = this.getRefreshToken();
    if (refresh) {
      this.api.logout(refresh).subscribe();
    }
    this.clearTokens();
    this.currentUserSubject.next(null);
  }

  isAuthenticated(): boolean {
    return !!this.getAccessToken();
  }

  getAccessToken(): string | null {
    return localStorage.getItem(this.accessTokenKey);
  }

  getRefreshToken(): string | null {
    return localStorage.getItem(this.refreshTokenKey);
  }

  private setTokens(access: string, refresh: string): void {
    localStorage.setItem(this.accessTokenKey, access);
    localStorage.setItem(this.refreshTokenKey, refresh);
  }

  private clearTokens(): void {
    localStorage.removeItem(this.accessTokenKey);
    localStorage.removeItem(this.refreshTokenKey);
  }
}
