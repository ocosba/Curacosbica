import { useEffect, useRef } from 'react';
import type { ReactNode } from 'react';

interface RevealProps {
  children: ReactNode;
  delay?: number;
  className?: string;
}

export function Reveal({ children, delay = 0, className = '' }: RevealProps) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    // Fallback: if IntersectionObserver is not supported, reveal immediately
    if (!window.IntersectionObserver) {
      el.classList.add('visible');
      return;
    }

    // Fail-safe fallback timer (forces reveal after 4 seconds if not triggered)
    const failSafeTimer = setTimeout(() => {
      el.classList.add('visible');
    }, 4000);

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          clearTimeout(failSafeTimer);
          setTimeout(() => {
            el.classList.add('visible');
          }, delay);
          observer.unobserve(el);
        }
      },
      {
        threshold: 0.1,
        rootMargin: '0px 0px -6% 0px',
      }
    );

    observer.observe(el);
    return () => {
      clearTimeout(failSafeTimer);
      observer.disconnect();
    };
  }, [delay]);

  return (
    <div ref={ref} className={`reveal ${className}`}>
      {children}
    </div>
  );
}
