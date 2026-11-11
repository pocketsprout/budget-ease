#!/usr/bin/env python3
"""Builds index.html (English) and es/index.html (Spanish) from
tools/home.template.html, so both languages always share one layout.

Run from the repository root:  python3 tools/build_home.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "tools" / "home.template.html").read_text(encoding="utf-8")


def icon(paths, size=22):
    return (
        f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
        'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f"{paths}</svg>"
    )


# Line icons (Lucide, ISC license) — shared by both languages.
ICONS = {
    "icon_wallet": icon('<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>'),
    "icon_shield": icon('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>'),
    "icon_target": icon('<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>'),
    "icon_card": icon('<rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/>'),
    "icon_tag": icon('<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>'),
    "icon_calculator": icon('<rect width="16" height="20" x="4" y="2" rx="2"/><line x1="8" x2="16" y1="6" y2="6"/><line x1="16" x2="16" y1="14" y2="18"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/>'),
    "icon_bell": icon('<path d="M10.268 21a2 2 0 0 0 3.464 0"/><path d="M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326"/>'),
    "icon_wifi_off": icon('<path d="M12 20h.01"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/><path d="M5 12.859a10 10 0 0 1 5.17-2.69"/><path d="M19 12.859a10 10 0 0 0-2.007-1.523"/><path d="M2 8.82a15 15 0 0 1 4.177-2.643"/><path d="M22 8.82a15 15 0 0 0-11.288-3.764"/><path d="m2 2 20 20"/>'),
    "icon_languages": icon('<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>'),
    "icon_mail": icon('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>', size=18),
}


def faq(items):
    out = []
    for question, answer in items:
        out.append(
            '      <div class="faq-item fade-up">\n'
            '        <button class="faq-question" onclick="toggleFaq(this)" aria-expanded="false">\n'
            f"          {question}\n"
            '          <span class="icon" aria-hidden="true">+</span>\n'
            "        </button>\n"
            f'        <div class="faq-answer">{answer}</div>\n'
            "      </div>"
        )
    return "\n\n".join(out)


EN = {
    "lang": "en",
    "root": "",
    "home": "./",
    "canonical": "https://pocketsprout.github.io/budget-ease/",
    "title": "Budget Ease — Know exactly where your money goes",
    "meta_description": "Budget Ease is a simple pocket budgeting app for iPhone and Android. Give every dollar a job, see what's safe to spend, track credit cards without double counting — offline, no account, free.",
    "og_title": "Budget Ease — Know exactly where your money goes",
    "og_description": "Simple pocket budgeting for iPhone and Android. Offline, no account, free.",
    "og_image": "og-image.png",
    "og_locale": "en_US",
    "by_pocket_sprout": "by Pocket Sprout",
    "nav_screens": "Screens",
    "nav_features": "Features",
    "nav_faq": "FAQ",
    "nav_support": "Support",
    "nav_privacy": "Privacy",
    "other_lang": "es",
    "other_lang_href": "es/",
    "other_lang_label": "ES",
    "other_lang_name": "Español",
    "hero_badge": "Now on iPhone &amp; Android",
    "hero_title": "Know exactly where your<br /><em>money goes</em>",
    "hero_sub": "Give every dollar a job, see what's safe to spend, and keep your data on your phone. No account, no subscription — just clarity about your finances.",
    "alt_app_store": "Download on the App Store",
    "alt_google_play": "Get it on Google Play",
    "play_badge": "google-play-badge.png",
    "play_badge_width": "181",
    "screens_label": "See it in action",
    "screens_title": "Your money, at a glance",
    "screens_desc": "Real screens from the app. Swipe through to see how it works.",
    "screens_aria": "App screenshots",
    "shot_dashboard": "dashboard.jpg",
    "shot_breakdown": "breakdown.jpg",
    "shot_entry": "entry.jpg",
    "shot_card": "card-default.jpg",
    "shot_transactions": "transactions.jpg",
    "shot_dashboard_alt": "Budget Ease dashboard showing Available Money of $1,284.48, Safe to Spend of $324.99 and savings goals",
    "shot_breakdown_alt": "Breakdown sheet showing how All Your Money becomes Available Money and Safe to Spend",
    "shot_entry_alt": "New transaction screen with a built-in calculator adding 36 + 12.5",
    "shot_card_alt": "Credit card setup explaining that a charge comes out of its pocket the moment you log it",
    "shot_transactions_alt": "Transaction list grouped by day with categories and pockets",
    "cap_dashboard_title": "Your dashboard",
    "cap_dashboard": "Available Money up top, with Safe to Spend and your savings goals right below.",
    "cap_breakdown_title": "The full math",
    "cap_breakdown": "Tap for details and see every goal and budget, step by step.",
    "cap_entry_title": "Built-in calculator",
    "cap_entry": "Type 36 + 12.50 right in the amount. No switching apps.",
    "cap_card_title": "Credit cards",
    "cap_card": "A card charge comes out of its pocket right away, so your budget stays honest.",
    "cap_transactions_title": "Every transaction",
    "cap_transactions": "Grouped by day, with the category and pocket for each one.",
    "features_label": "What makes it different",
    "features_title": "Built for real budgets,<br />real families",
    "features_desc": "Every feature in Budget Ease is designed around one idea: you should always know exactly how much you can spend.",
    "new_tag": "NEW",
    "f_pockets_title": "Pockets for everything",
    "f_pockets": "Split your money into spending pockets like Groceries or Dining, and savings goals like an Emergency Fund. Every dollar gets a job before you spend it.",
    "f_safe_title": "Know what you can spend",
    "f_safe": "Available Money is everything not set aside for savings. Safe to Spend goes one step further: the money no budget or goal has claimed yet.",
    "f_goals_title": "Savings goals",
    "f_goals": "Set a target and watch the progress bar fill. Got paid? Move money straight into a goal with one transfer.",
    "f_cards_title": "Credit cards, simplified",
    "f_cards": "Log a card purchase like cash — it comes out of its pocket right away. Budget Ease keeps track of what you still owe the bank, and paying the bill never counts the money twice.",
    "f_categories_title": "Categories",
    "f_categories": "Groceries, Dining, Transport and more — or create your own with an emoji and a color. Filter your history by category any time.",
    "f_calculator_title": "Built-in calculator",
    "f_calculator": "Add up a split bill or a few items right where you type the amount. The keypad does the math for you.",
    "f_reminders_title": "Daily reminders",
    "f_reminders": "A gentle nudge at the time you choose, so logging the day's spending becomes a habit.",
    "f_offline_title": "Private &amp; offline",
    "f_offline": "No internet needed and no account to create. Your data lives on your phone — private, fast and always available.",
    "f_language_title": "English &amp; Spanish",
    "f_language": "Every screen is available in English and Spanish. The app automatically uses your phone's language.",
    "faq_label": "Support",
    "faq_title": "Common questions",
    "faq_desc": "Everything you need to get started with Budget Ease.",
    "faq_items": faq([
        ("Is Budget Ease free?",
         "Yes — Budget Ease is completely free to download and use. There are no subscriptions, no in-app purchases and no hidden fees. Every feature is available from the moment you open the app."),
        ("Do I need to create an account?",
         "No account required. Budget Ease works fully offline — your data is stored on your device. Nothing is sent to any server, and no personal information is collected."),
        ("Does it connect to my bank?",
         "No. You log your transactions yourself, which takes a few seconds with the built-in calculator. That means no bank logins, no card numbers and nothing shared with anyone."),
        ("What's the difference between Available Money and Safe to Spend?",
         "Your dashboard shows two numbers. Available Money is everything you have minus what's set aside in savings goals. Safe to Spend goes one step further and also subtracts what's left in your spending pockets — it's the money that isn't budgeted for anything yet, so you can spend it without touching a budget or a goal. Tap the card on the dashboard to see the full math."),
        ("How do credit cards work in Budget Ease?",
         "Log a card purchase like any other expense and choose the card under “Paid with.” The money comes out of its pocket right away, just like cash, so your budget is always accurate. The card keeps a list of the charges you haven't paid the bank back for yet. When you pay your card bill, record the payment on the card: it marks those charges as paid and never counts the money twice."),
        ("How do I reset a Pocket?",
         "Open the spending pocket you want to reset, tap the options menu and choose “Reset Pocket.” This clears all transactions in that pocket and restores its full budget. Savings pockets can't be reset — their balance carries over indefinitely."),
        ("Is Budget Ease available on iPhone?",
         "Yes! Budget Ease is available for iPhone and iPad on the App Store, and for Android on Google Play."),
        ("How do I change the language?",
         "Budget Ease uses your phone's language: if your phone is set to Spanish, the app is in Spanish; otherwise it's in English. To switch, change your phone's language in its settings."),
        ("Is my data backed up?",
         "There's no cloud sync — your data stays on your phone. Your phone's own backup (iCloud or Google) may include it. If you delete the app and have no backup, your data is deleted with it."),
    ]),
    "contact_label": "Get in touch",
    "contact_title": "Need help?",
    "contact_box_title": "We're here for you",
    "contact_box_text": "Have a question, found a bug, or want to share feedback? Reach out directly — we read every message and respond as quickly as we can.",
    "rights": "All rights reserved.",
    "footer_privacy": "Privacy Policy",
    "footer_contact": "Contact",
}

ES = {
    "lang": "es",
    "root": "../",
    "home": "./",
    "canonical": "https://pocketsprout.github.io/budget-ease/es/",
    "title": "Budget Ease — Sabe exactamente a dónde va tu dinero",
    "meta_description": "Budget Ease es una app sencilla de presupuesto por bolsillos para iPhone y Android. Dale un propósito a tu dinero, mira cuánto puedes gastar y controla tus tarjetas de crédito sin contar doble — sin internet, sin cuenta y gratis.",
    "og_title": "Budget Ease — Sabe exactamente a dónde va tu dinero",
    "og_description": "Presupuesto por bolsillos, fácil, para iPhone y Android. Sin internet, sin cuenta y gratis.",
    "og_image": "og-image-es.png",
    "og_locale": "es_LA",
    "by_pocket_sprout": "por Pocket Sprout",
    "nav_screens": "Pantallas",
    "nav_features": "Funciones",
    "nav_faq": "Preguntas",
    "nav_support": "Soporte",
    "nav_privacy": "Privacidad",
    "other_lang": "en",
    "other_lang_href": "../",
    "other_lang_label": "EN",
    "other_lang_name": "English",
    "hero_badge": "Ya en iPhone y Android",
    "hero_title": "Sabe exactamente a dónde<br /><em>va tu dinero</em>",
    "hero_sub": "Dale un propósito a tu dinero, mira cuánto puedes gastar y guarda tus datos en tu teléfono. Sin cuenta, sin suscripción — solo claridad sobre tus finanzas.",
    "alt_app_store": "Descárgalo en el App Store",
    "alt_google_play": "Disponible en Google Play",
    "play_badge": "google-play-badge-es.png",
    "play_badge_width": "182",
    "screens_label": "Míralo en acción",
    "screens_title": "Tu dinero, de un vistazo",
    "screens_desc": "Pantallas reales de la app (en inglés). Deslízalas para ver cómo funciona; en tu teléfono la verás en español.",
    "screens_aria": "Capturas de pantalla de la app",
    "shot_dashboard": "dashboard.jpg",
    "shot_breakdown": "breakdown.jpg",
    "shot_entry": "entry.jpg",
    "shot_card": "card-default.jpg",
    "shot_transactions": "transactions.jpg",
    "shot_dashboard_alt": "Panel de Budget Ease con Dinero Disponible de $1,284.48, Disponible para Gastar de $324.99 y metas de ahorro",
    "shot_breakdown_alt": "Detalle que muestra cómo Todo Tu Dinero se convierte en Dinero Disponible y Disponible para Gastar",
    "shot_entry_alt": "Pantalla de nueva transacción con una calculadora integrada sumando 36 + 12.5",
    "shot_card_alt": "Configuración de tarjeta de crédito que explica que un cargo sale de su bolsillo en cuanto lo registras",
    "shot_transactions_alt": "Lista de transacciones agrupadas por día con categorías y bolsillos",
    "cap_dashboard_title": "Tu panel",
    "cap_dashboard": "Dinero Disponible arriba, con Disponible para Gastar y tus metas de ahorro justo debajo.",
    "cap_breakdown_title": "Las cuentas completas",
    "cap_breakdown": "Toca para ver el detalle de cada meta y presupuesto, paso a paso.",
    "cap_entry_title": "Calculadora integrada",
    "cap_entry": "Escribe 36 + 12.50 directo en el monto. Sin cambiar de app.",
    "cap_card_title": "Tarjetas de crédito",
    "cap_card": "Un cargo con tarjeta sale de su bolsillo al instante, así tu presupuesto siempre es real.",
    "cap_transactions_title": "Cada transacción",
    "cap_transactions": "Agrupadas por día, con la categoría y el bolsillo de cada una.",
    "features_label": "Lo que la hace diferente",
    "features_title": "Hecha para presupuestos reales,<br />familias reales",
    "features_desc": "Cada función de Budget Ease gira en torno a una idea: siempre deberías saber exactamente cuánto puedes gastar.",
    "new_tag": "NUEVO",
    "f_pockets_title": "Bolsillos para todo",
    "f_pockets": "Divide tu dinero en bolsillos de gastos como Mercado o Restaurantes, y metas de ahorro como un Fondo de Emergencia. Cada centavo tiene un propósito antes de gastarlo.",
    "f_safe_title": "Sabe cuánto puedes gastar",
    "f_safe": "Dinero Disponible es todo lo que no está apartado para ahorros. Disponible para Gastar va un paso más allá: es el dinero que ningún presupuesto ni meta ha reservado todavía.",
    "f_goals_title": "Metas de ahorro",
    "f_goals": "Ponte una meta y mira cómo se llena la barra de progreso. ¿Te pagaron? Pasa dinero directo a una meta con una sola transferencia.",
    "f_cards_title": "Tarjetas de crédito, sin enredos",
    "f_cards": "Registra una compra con tarjeta como si fuera efectivo: sale de su bolsillo al instante. Budget Ease lleva la cuenta de lo que aún le debes al banco, y pagar la tarjeta nunca cuenta el dinero dos veces.",
    "f_categories_title": "Categorías",
    "f_categories": "Mercado, Restaurantes, Transporte y más — o crea las tuyas con un emoji y un color. Filtra tu historial por categoría cuando quieras.",
    "f_calculator_title": "Calculadora integrada",
    "f_calculator": "Suma una cuenta dividida o varias compras justo donde escribes el monto. El teclado hace las cuentas por ti.",
    "f_reminders_title": "Recordatorios diarios",
    "f_reminders": "Un recordatorio amable a la hora que elijas, para que anotar tus gastos del día se vuelva un hábito.",
    "f_offline_title": "Privada y sin internet",
    "f_offline": "No necesita internet ni una cuenta. Tus datos viven en tu teléfono: privados, rápidos y siempre disponibles.",
    "f_language_title": "Español e inglés",
    "f_language": "Todas las pantallas están en español y en inglés. La app usa automáticamente el idioma de tu teléfono.",
    "faq_label": "Soporte",
    "faq_title": "Preguntas frecuentes",
    "faq_desc": "Todo lo que necesitas para empezar con Budget Ease.",
    "faq_items": faq([
        ("¿Budget Ease es gratis?",
         "Sí. Budget Ease es completamente gratis para descargar y usar. No tiene suscripciones, compras dentro de la app ni cobros ocultos. Todas las funciones están disponibles desde que abres la app."),
        ("¿Necesito crear una cuenta?",
         "No. Budget Ease funciona totalmente sin internet y tus datos se guardan en tu teléfono. No se envía nada a ningún servidor y no se recopila información personal."),
        ("¿Se conecta a mi banco?",
         "No. Tú registras tus transacciones, y con la calculadora integrada toma solo unos segundos. Eso significa que no hay claves del banco, ni números de tarjeta, ni nada compartido con nadie."),
        ("¿Cuál es la diferencia entre Dinero Disponible y Disponible para Gastar?",
         "Tu panel muestra dos números. Dinero Disponible es todo tu dinero menos lo que está apartado en metas de ahorro. Disponible para Gastar va un paso más allá y también resta lo que queda en tus bolsillos de gastos: es el dinero que todavía no tiene ningún propósito, así que puedes gastarlo sin tocar un presupuesto ni una meta. Toca la tarjeta del panel para ver las cuentas completas."),
        ("¿Cómo funcionan las tarjetas de crédito en Budget Ease?",
         "Registra una compra con tarjeta como cualquier otro gasto y elige la tarjeta en “Pagado con”. El dinero sale de su bolsillo al instante, igual que el efectivo, así tu presupuesto siempre está al día. La tarjeta guarda la lista de los cargos que todavía no le has pagado al banco. Cuando pagues la tarjeta, registra el pago en ella: marca esos cargos como pagados y nunca cuenta el dinero dos veces."),
        ("¿Cómo reinicio un bolsillo?",
         "Abre el bolsillo de gastos que quieres reiniciar, toca el menú de opciones y elige “Reiniciar Bolsillo”. Esto borra todas las transacciones de ese bolsillo y le devuelve su presupuesto completo. Los bolsillos de ahorro no se pueden reiniciar: su saldo se conserva siempre."),
        ("¿Budget Ease está disponible para iPhone?",
         "¡Sí! Budget Ease está disponible para iPhone y iPad en el App Store, y para Android en Google Play."),
        ("¿Cómo cambio el idioma?",
         "Budget Ease usa el idioma de tu teléfono: si tu teléfono está en español, la app está en español; si no, está en inglés. Para cambiarlo, cambia el idioma en los ajustes de tu teléfono."),
        ("¿Se hace copia de seguridad de mis datos?",
         "No hay sincronización en la nube: tus datos se quedan en tu teléfono. La copia de seguridad de tu propio teléfono (iCloud o Google) puede incluirlos. Si borras la app y no tienes copia de seguridad, tus datos se borran con ella."),
    ]),
    "contact_label": "Contáctanos",
    "contact_title": "¿Necesitas ayuda?",
    "contact_box_title": "Estamos para ayudarte",
    "contact_box_text": "¿Tienes una pregunta, encontraste un error o quieres darnos tu opinión? Escríbenos directamente — leemos cada mensaje y respondemos lo más rápido posible.",
    "rights": "Todos los derechos reservados.",
    "footer_privacy": "Política de privacidad",
    "footer_contact": "Contacto",
}


def render(strings):
    html = TEMPLATE
    for key, value in {**ICONS, **strings}.items():
        html = html.replace(f"[[{key}]]", value)
    leftover = [part.split("]]")[0] for part in html.split("[[")[1:]]
    if leftover:
        raise SystemExit(f"Unfilled placeholders: {sorted(set(leftover))}")
    return html


(ROOT / "index.html").write_text(render(EN), encoding="utf-8")
(ROOT / "es").mkdir(exist_ok=True)
(ROOT / "es" / "index.html").write_text(render(ES), encoding="utf-8")
print("Wrote index.html and es/index.html")
