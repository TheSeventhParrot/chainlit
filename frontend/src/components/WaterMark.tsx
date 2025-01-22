import { Translator } from 'components/i18n';

import 'assets/Red Logo.svg';
import LogoDark from 'assets/Red Logo.svg?react';
import 'assets/Logo.svg';
import LogoLight from 'assets/Logo.svg?react';

import { useTheme } from './ThemeProvider';

export default function WaterMark() {
  const { variant } = useTheme();
  const Logo = variant === 'light' ? LogoLight : LogoDark;

  return (
    <a
      href="https://www.promptinversion.ai/"
      target="_blank"
      className="watermark"
      style={{
        display: 'flex',
        alignItems: 'center',
        textDecoration: 'none'
      }}
    >
      <div className="text-xs text-muted-foreground">
        <Translator path="components.organisms.chat.inputBox.waterMark.text" />
      </div>
      <Logo
        style={{
          width: 65,
          height: 'auto',
          filter: 'grayscale(1)',
          marginLeft: '4px'
        }}
      />
    </a>
  );
}
