Editor
Editando archivo
qwen2-translator-web/client/src/pages/Home.tsx
Home.tsx
Diferencia
Original
Modificado
import TranslatorWidget from "@/components/TranslatorWidget";
import { Button } from "@/components/ui/button";
import { Globe, Code2, Zap } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen bg-white text-foreground">
      {/* Navigation */}
      <nav className="sticky top-0 z-50 bg-white border-b border-border">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-gradient-to-br from-cyan-400 to-cyan-600 rounded-lg flex items-center justify-center">
              <Globe className="w-5 h-5 text-white" />
            </div>
            <h1 className="text-xl font-bold text-foreground">Qwen2 Translator</h1>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative overflow-hidden py-12 lg:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-4">
              Traducción de IA Local
            </h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
              Traduce texto de inglés a 10 idiomas usando IA. 100% local, sin APIs externas, sin claves de servicios.
            </p>
          </div>
        </div>
      </section>

      {/* Translator Widget */}
      <section className="bg-secondary/30 py-12 lg:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <TranslatorWidget />
        </div>
      </section>

      {/* Features Section */}
      <section className="py-12 lg:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-foreground mb-12 text-center">
            Características
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white border-l-4 border-l-primary p-6 rounded-lg">
              <Code2 className="w-10 h-10 text-primary mb-4" />
              <h3 className="text-xl font-bold text-foreground mb-2">100% Local</h3>
              <p className="text-muted-foreground">
                El modelo se ejecuta completamente en tu navegador. Sin conexión a internet requerida después de la carga inicial.
              </p>
            </div>
            <div className="bg-white border-l-4 border-l-primary p-6 rounded-lg">
              <Globe className="w-10 h-10 text-primary mb-4" />
              <h3 className="text-xl font-bold text-foreground mb-2">10 Idiomas</h3>
              <p className="text-muted-foreground">
                Español, Francés, Alemán, Italiano, Portugués, Chino, Japonés, Árabe, Ruso e Hindi.
              </p>
            </div>
            <div className="bg-white border-l-4 border-l-primary p-6 rounded-lg">
              <Zap className="w-10 h-10 text-primary mb-4" />
              <h3 className="text-xl font-bold text-foreground mb-2">Rápido</h3>
              <p className="text-muted-foreground">
                Interfaz intuitiva con historial de traducciones y atajos de teclado para máxima productividad.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-foreground text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p>© 2026 Qwen2 Translator. Traducción local impulsada por IA.</p>
        </div>
      </footer>
    </div>
  );
}
