import { Injectable } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class TranslationService {
  constructor(private translate: TranslateService, private http: HttpClient) {}

  init() {
    this.translate.setDefaultLang('en');
    this.translate.use('en');

    // Load translations dynamically using HttpClient
    this.loadTranslations('en').subscribe((translations: any) => {
      this.translate.setTranslation('en', translations);
    });

    this.loadTranslations('fr').subscribe((translations: any) => {
      this.translate.setTranslation('fr', translations);
    });
  }

  changeLang(lang: string) {
    this.translate.use(lang);
  }

  private loadTranslations(lang: string) {
    return this.http
      .get(`src/locale/messages.${lang}.json`)
      .pipe(map((res: any) => res.default));
  }
}
