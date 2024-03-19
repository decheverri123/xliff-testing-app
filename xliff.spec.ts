import { TestBed } from '@angular/core/testing';
import * as fs from 'fs';
import * as xml2js from 'xml2js';
import { TranslateModule, TranslateService } from '@ngx-translate/core';

describe('Translation file (.xlf) tests', () => {
  let parser: xml2js.Parser;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    parser = new xml2js.Parser();
  });

  it('should validate the structure of the XLF file', (done) => {
    fs.readFile('src/locale/messages.xlf', 'utf8', (err, data) => {
      if (err) throw err;

      parser.parseString(data, (error, result) => {
        if (error) throw error;

        expect(result).toBeTruthy();
        expect(result.xliff).toBeTruthy();
        expect(result.xliff.file).toBeTruthy();
        done();
      });
    });
  });

  // Add more tests as needed
});
